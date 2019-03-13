curl -H "Host: data.usajobs.gov" \
-H "User-Agent: turbohoje@hotmail.com" \
-H "Authorization-Key: F+l0s0ygdz40th9Mb7Xyrib4Nhnql3NDGfBNAVP3LFI=" \
'https://data.usajobs.gov/api/search?LocationName=Aurora,%20Colorado&Radius=0&PositionScheduleTypeCode=1&ResultsPerPage=100' | jq ".SearchResult.SearchResultItems[].MatchedObjectDescriptor.PositionTitle"

