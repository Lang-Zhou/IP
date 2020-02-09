# IP
A Python substitution for getting IP address and relating information.

***Notice: This program works due to the existence of wtfismyip.com. All my work is just processing the data crawled from this service.***

***According to the WTFPL license of the wtfismyip project on Github, this program is for non-commercial use.***

## Guide
### Install
```
pip3 install IP-1.0.tar.gz
```
Environment requirement: Python version 3.7.3 or higher.

The sorce code is also provided for those who would like to compile themselves.

Don't want to use it anymore? Just
```
pip3 uninstall IP
```
### How to use
First,
```
import IP
```
The program offers 3 functions in general, which are IP.show(), IP.overall(), IP.get().
Any exceptions or errors will make all the functions below return -1.
#### show()
Directly print all the data

Example:
```
>>>IP.show()
IP Address: 47.75.94.122
Host Name: 47.75.94.122
IP Location: Central, HCW, Hong Kong
Country Code: HK
ISP: Alibaba
Is Tor Exit: False
```
#### overall()
Return a dictionary containing overall data.

Example:
```
>>>print(IP.overall())
{'IP': '47.75.94.122', 'Host': '47.75.94.122', 'Location': 'Central, HCW, Hong Kong', 'Code': 'HK', 'ISP': 'Alibaba', 'Tor': False}
```
#### get()
Return a string containing specific data requested by the get(), if didn't specialize any string for requests, return IP address by default.

|String for get() request|Request target|
| ---- | ---- |
|'IP'|IP Address|
|'Host'|Host Name|
|'Location'|IP Location|
|'Code'|Country Code|
|'ISP'|ISP|
|'Tor'|Is Tor Exit|

Example:
```
>>>IP.get('ISP')
Alibaba
```
### Notice
Due to the rules set by wtfismyip.com, too frequent use of this program may lead to your IP being temporarily blocked, so please use it moderately.

***The stability of this service cannot be guaranteed.***

Issues are welcome. Should you find any bug, you can also mail me to <zhoulang731@gmail.com>
