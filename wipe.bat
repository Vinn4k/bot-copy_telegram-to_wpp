@echo off
echo Este script irá apagar os seguintes arquivos e pastas:
echo - Pasta "User Data"
echo - Arquivo "config.json"
echo - Arquivo "projectGeremias.session"
echo.

echo - Apagando Pasta "Dados do navegador"
rd /s /q "User Data"
echo -Aagando Arquivo de configuração
del /f /s /q "config.json"
echo - Apagando Arquivo de sessão do telegram
del /f /s /q "projectGeremias.session"

pause

