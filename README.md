This is a proxy script for fetching CRN data from NCDC server using a restful
syntax compatible with [Multigraph](http://multigraph.org).

This script accepts URLs of the form:

```
http://..../data/STATION_ID/ELEMENT_LIST/START_TIME,END_TYPE
```

for example, with specific values:

```
http://..../data/1026/T5,P5/2015030108,2015030109
```

and produces output like this:

```
201503010800,.52,0
201503010805,.59,0
201503010810,.47,0
201503010815,.34,0
201503010820,.23,0
201503010825,.17,0
201503010830,.05,0
201503010835,-.02,0
201503010840,-.02,0
201503010845,-.05,0
201503010850,-.06,0
201503010855,-.06,0
201503010900,-.05,0
```
