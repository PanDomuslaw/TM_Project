# REST-Api-ivectors
ivector REST api

Do prawidłowego działania należy pobrać paczkę z folderem z modelami,
dostępną tutaj: https://www.voicebiometry.org/

Następnie folder ivector -> zamienić na ten z GitHuba (ivector-python-master)

DONE:
- struktura obiektowa dla generacji ivectorów (klasa IVector), zamiana skryptu z Brno na klasę z metodami,
- podstawowa struktura API w frameworku Flask, z ustalonymi endpointami,
- działające na localhost, REST-API,
- napisanie prostego Clienta,
- dane są zwracane w plikach .json

TODO:
- system tokenów,
- deploy na Dockerze,
- wielowątkowość,
- wysyłanie pliku w postaci binarnej.
