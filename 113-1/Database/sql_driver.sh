
# 1. Install ODBC Driver 17 for SQL Server (Arch Linux)
sudo curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo pacman-key --add -
sudo pacman-key --lsign-key EB3E94ADBE1229CF

sudo pacman -S unixodbc

odbcinst -j

# 2. Install the ODBC Driver for SQL Server
yay -S msodbcsql17


# 3. Verify Installation
odbcinst -q -d


