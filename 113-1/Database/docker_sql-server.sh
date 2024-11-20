sudo docker pull mcr.microsoft.com/mssql/server:2022-latest

docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Password1234" \
   -p 1433:1433 --name sql1 --hostname sql1 \
   -d \
   mcr.microsoft.com/mssql/server:2022-latest

# 5c5cc2cd1bc7a1b1a3039524bff6fa11f049a6e0e35aad82d05014e9561b0216
