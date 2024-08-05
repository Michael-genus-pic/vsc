* 5 dockers
  * animal api
  * litter api
  * notification api
  * queueprocessor
  * dispatcher accessor to the apis

`commands.txt` shows all commands


api calls: 
* animal.AddAnimal()
  * (async) call litter.AddPigletToLitter
* litter.getLitterMatesbyLitterId()
  * call animal.Getanimalbylitterid
* litter.addPigletToLitter()
  * call animal.Getanimalbyid


![Components](components.png)
