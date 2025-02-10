# Cantera Helper

This repository provides a starter example for using Cantera to run an O<sub>2</sub> sweep.


## 1. General Set-up
### Set up a Linux terminal

If you are on a Windows machine, follow these instructions to install the Windows Subsystem for Linux (WSL):
1. Open PowerShell in administrator mode by right-clicking and selecting "Run as administrator".
2. Enter the following command into the command prompt:
   ```
   wsl --install
   ```
3. Re-start your machine.

This creates a miniature Linux operating system (OS) on your computer, which you can access through a terminal. You can can open this Linux terminal by searching "WSL" in your taskbar clicking "Open". You can also click "Pin to taskbar" for easier access.
You only need to do this once.


### Install Pixi

This project uses the [Pixi](https://pixi.sh/latest/) package manager. You can install it by opening up your WSL terminal and running the following command:
```
curl -fsSL https://pixi.sh/install.sh | bash
```
You only need to do this once.

## 2. Setting up this repository

All of the files you need are in this repository, which you can download as follows.[^1]
```
git clone https://github.com/rotavera-group/cantera-helper.git
```
You can then enter the repotisory and install the necessary dependencies as follows.
```
cd cantera-helper/
pixi install
```
From now on, you can activate the environment in this repository using `pixi shell`.

## 3. Running the example

To run the starter example, you can simply do the following:
```
cd example/     # Navigate to example
pixi shell      # Activate environment
python run.py   # Run simulation!
```
The 


[^1]: The `git clone` command can conflict with VPN, so you may need to temporarily turn the latter off if you have it running in the background. Fortunately, you only need to do this step once.
