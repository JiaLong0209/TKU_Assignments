
# 
https://blog.csdn.net/weixin_29781865/article/details/153959122

## Wine
在 Linux 上使用 Wine 進行音樂製作時，安裝正確的 Windows 組件（Runtime Libraries） 是確保 VST 插件與 DAW（如 REAPER）穩定的關鍵。Wine 雖然強大，但在處理複雜的 GUI 渲染、授權驗證（DRM） 與 多執行緒通訊 時，內建的開源實作（Builtin）往往不夠完整。
以下是製作音樂時必備的 Windows 組件清單及其功能說明：
1. 核心運行庫 (Visual C++ Redistributable)
這是大多數 VST 插件（如 Kontakt, Serum, FabFilter）的基礎。

* 組件名稱：vcredist2015, vcredist2017, vcredist2019, vcredist2022
* 指令：winetricks -q vcredist2015 vcredist2017 vcredist2019 vcredist2022
* 為什麼需要：
* 代碼執行：開發者使用 Microsoft Visual Studio 編寫插件，這些 DLL（如 msvcp140.dll）包含了插件運行所需的基礎指令集。
   * 防止崩潰：如果缺失，加載 VST 時會直接報錯 Runtime Error 或找不到 DLL。

2. 介面渲染組件 (DirectX & GDI+)
解決插件介面黑屏、白屏、閃爍或 GUI 無法顯示的問題。

* 組件名稱：d3dcompiler_47, d2d1, gdiplus
* 指令：winetricks -q d3dcompiler_47 d2d1 gdiplus
* 為什麼需要：
* 硬體加速：現代 VST（如 Soundpaint, SINE）使用 GPU 渲染介面。d3dcompiler_47 是 Direct3D 的著色器編譯器，沒它就畫不出圖案。
   * 向量繪圖：gdiplus 用於處理舊式插件的平滑文字與圖形。

3. 網路與授權驗證 (Networking & DRM)
解決 Native Access, Splice, iLok, Waves Central 等管理軟體無法連網或登入的問題。

* 組件名稱：winhttp, wininet, win10 (版本偽裝)
* 指令：winetricks -q winhttp wininet
* 為什麼需要：
* 加密通訊：解決 secur32 報錯（unknown algorithm）。原生 DLL 支援更完整的 SSL/TLS 加密，讓授權驗證能通過。
   * 背景下載：確保安裝程式能正確下載音色包（Sample Libraries）。

4. 字體庫 (Core Fonts)
解決插件介面文字變亂碼或因為找不到字體而閃退。

* 組件名稱：corefonts, cjkfonts
* 指令：winetricks -q corefonts
* 為什麼需要：
* UI 佈局：許多插件（如 Spitfire）如果找不到 Arial 或 Segoe UI 等字體，會因為無法計算 UI 大小而直接崩潰或顯示異常。

5. .NET Framework (特定插件需求)
針對某些使用 .NET 技術開發的管理工具（如舊版 Native Access）。

* 組件名稱：dotnet48
* 指令：winetricks -q dotnet48
* 為什麼需要：
* 系統框架：.NET 是 Windows 獨有的開發框架，Wine 的內建替代品（Mono）有時無法執行複雜的數據庫操作。

------------------------------
大補帖：一鍵安裝指令（適用於新的 WINEPREFIX）
如果你建立了一個新的環境，想一次搞定：

WINEPREFIX=~/.wine64 winetricks -q vcredist2015 vcredist2017 vcredist2019 vcredist2022 d3dcompiler_47 d2d1 gdiplus corefonts winhttp wininet

進階提示：DXVK
雖然這不是透過 winetricks 安裝的標準 Windows 組件，但它是 Linux 音樂製作的靈魂。

* 作用：將 VST 的 DirectX 渲染轉換為 Vulkan。
* 好處：極大提升 GUI 流暢度，解決 NVIDIA 顯卡在 Wine 下的視窗延遲。
* 安裝：WINEPREFIX=~/.wine64 winetricks dxvk

您目前使用的 .wine64 環境中，是否已經安裝過 vcredist 系列了？ 這通常是解決 90% 插件啟動失敗的第一步。


## limits

你提供的 /etc/security/limits.conf 目前全是註解（以 # 開頭），這代表系統尚未對音訊實時處理進行最佳化。對於管弦樂編組（大量採樣、高內存佔用）來說，這會導致 Wine/yabridge 在處理 Soundpaint 等大型插件時頻繁出現超時或內存鎖定錯誤。
請按照以下步驟修改，以賦予 REAPER 和 Wine 所需的權限：
1. 編輯設定檔
在終端機輸入：

sudo micro /etc/security/limits.conf

(如果你習慣用 nano 或 vim 也可以)
2. 加入實時權限設定
捲動到檔案最下方，貼上以下內容：

@realtime - rtprio 98
@realtime - memlock unlimited
@realtime - nice -11


* rtprio 98：允許音訊線程擁有極高的優先權，防止爆音（Xruns）。
* memlock unlimited：允許 Soundpaint 直接鎖定 RAM，這對管弦樂採樣器至關重要，能避免因內存分頁交換導致的崩潰。

3. 建立群組並加入你的帳號
輸入以下指令：

# 建立 realtime 群組 (若已存在會顯示提示，沒關係)
sudo groupadd realtime
# 將你自己加入群組 ($USER 會自動帶入你的用戶名)
sudo gpasswd -a $USER realtime

4. 關鍵一步：檢查 /etc/security/limits.d/
你的檔案註解提到，/etc/security/limits.d/ 資料夾內的設定會覆蓋此檔案。
Garuda Linux 通常會預裝 performance-tweaks。請檢查該目錄下是否有檔案：

ls /etc/security/limits.d/

如果裡面有 99-realtime-privileges.conf 之類的檔案，請確保裡面的數值與上述一致，或者直接在該目錄下建立新檔。
5. 重新開機
這非常重要！ 修改 limits.conf 後，必須登出再登入或直接重新開機，權限才會生效。
------------------------------
重啟後的檢查
開機後，在終端機輸入：

ulimit -r -l


* 若看到 real-time priority 98 且 max locked memory unlimited，表示設定成功。

補充建議：
由於 Soundpaint 的 Log 顯示它在嘗試 BCrypt（加密）時崩潰，請務必同時確認已安裝 lib32-gnutls：

sudo pacman -S gnutls lib32-gnutls

完成這些設定後，嘗試重新打開 REAPER，看看 Soundpaint 是否還會導致 JACK/PipeWire 斷開連接？

## iwlwifi


這份 Log 揭露了一個非常嚴重的底層問題：你的無線網卡驅動 (iwlwifi) 發生了核心崩潰 (Kernel Panic/Taint)，這直接導致了整個系統（包括 KDE 和 REAPER）的凍結與崩潰。
這解釋了為什麼你會遇到「KDE 突然凍結」和「切換 TTY 後 REAPER 自行關閉」。當核心驅動出錯時，系統會嘗試進入安全狀態或發生中斷，進而踢掉所有的使用者行程。
為什麼這會影響到 REAPER？

   1. 實時衝突：在管弦樂編組中，REAPER 要求極高的音訊優先權。當 iwlwifi 因為 SYSTEM_STATISTICS_CMD 超時而鎖死 CPU 核心時，音訊引擎會立刻崩潰。
   2. Soundpaint 的網路檢查：你之前提到的 Soundpaint 插件一直在調用網路驗證，這可能頻繁觸發了已經不穩定的網卡驅動，導致核心直接「切掉」連線，進而引發 std::system_error。

建議解決方案（按優先順序）：1. 禁用無線網卡的節能模式 (最推薦)
Intel 的網卡（iwlwifi）在 Linux 下常因為節能切換導致超時。

* 建立一個設定檔：

sudo micro /etc/modprobe.d/iwlwifi.conf

* 貼入以下內容：

options iwlwifi power_save=0
options iwlmvm power_scheme=1

* 儲存後重新開機。這能防止網卡因為頻繁進入省電狀態而導致核心超時。

2. 製作音樂時關閉 Wi-Fi
既然你是做管弦樂這種重負載工作，核心穩定性高於一切。

* 在開啟 REAPER 前，先在 KDE 系統匣或使用指令關閉網路：

nmcli radio wifi off

這能完全避免 iwlwifi 驅動在後台作怪。

3. 更新或更換核心 (Kernel)
你的 Log 顯示核心版本是 6.18 (或類似)，這在 Garuda 這種滾動更新發行版中可能存在特定硬體相容問題。

* 嘗試安裝 linux-zen 核心（對音訊優化更好且通常包含較新的驅動修復）：

sudo pacman -S linux-zen linux-zen-headers

* 安裝後重新開機，並在 Grub 選單中選擇進入 zen 核心。

4. 關於 REAPER 的 Core Dump
目前的 reaper dumped core 只是網卡崩潰後的結果。只要解決了 iwlwifi 的問題，REAPER 的崩潰大概率會消失。
總結建議：
你這台 MSI Sword 17 的網卡驅動目前在 Linux 核心中非常不穩定。請先執行 步驟 1 禁用網卡節能，這通常能解決 90% 的 iwlwifi 核心超時問題。
如果你現在關閉 Wi-Fi 使用 REAPER，還會發生 KDE 凍結的情況嗎？

