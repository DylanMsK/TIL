# Chocolatey

#### 1. window cmd 관리자 원한으로 열기

#### 2. Chocolatey 설치

 1. [chocolatey.org](https://chocolatey.org/install)에서 **Install with cmd.exe** 복붙

    ```bash
    > @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    ```

	2. `> choco--versions `로 버전 확인

	3. ` > choco search <package-name>`으로 설치하려는 패키지 검색

	4. `> choco install <package-name [--version x.x.x]>`로 패키지 설치

    ex) `> choco install python --version 3.6.7` 

