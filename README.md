data.multigraph.org
===================

This project contains several proxy scripts for fetching data using a restful
syntax compatible with Multigraph.


crn
---

This script accepts URLs of the form:

```
http://data.multigraph.org/crn/STATION_ID/ELEMENT_LIST/START_TIME,END_TYPE
```

for example, with specific values:

```
http://data.multigraph.org/crn/1026/T5,P5/2015030108,2015030109
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

acis
----

This script accepts URLs of the form

```
http://data.multigraph.org/acis/SID/ELEMS/SDATE,EDATE
```

for example, with specific values:

```
http://data.multigraph.org/acis/13881-1/maxt,mint,normal_maxt,normal_mint/20120920000000,20120927000000
```
