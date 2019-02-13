https://www.pge.com/includes/docs/pdfs/myhome/addservices/moreservices/sharemydata/SOAP_UI_Steps.pdf

https://docs.gitlab.com/ee/api/project_import_export.html
importrequests
import urllib
import json
import sys

s3_file=urllib.urlopen(presigned_url)

url='https://gitlab.example.com/api/v4/projects/import'
files={'file':s3_file}
data={
"path":"example-project",
"namespace":"example-group"
}
headers={
'Private-Token':"9koXpg98eAheJpvBs5tK"
}

requests.post(url,headers=headers,data=data,files=files)



import requests
res = requests.get('https://<IPADDRESSGITSOURCE>/users?active=true')

#https://curl.trillworks.com/#
'''
import requests
headers = {
    'Authorization': 'Bearer OAUTH-TOKEN',
}
response = requests.get('https://<IPADDRESSGITSOURCE>/users?active=true', headers=headers)
'''
curl  --header "Authorization: Bearer OAUTH-TOKEN" https://<IPADDRESSGITSOURCE>/users?active=true | python -c 'import sys, json; print json.load(sys.stdin)["username"]
curl  --header "Authorization: Bearer OAUTH-TOKEN" https://<IPADDRESSGITSOURCE>/users?active=true | python -c 'import sys, json; print json.load(sys.stdin)["ename"]

Request type
Description
GET Access one or more resources and return the result as JSON.
POST Return 201 Created if the resource is successfully created and return the newly created resource as JSON.
GET / PUT  Return 200 OK if the resource is accessed or modified successfully. The (modified) result is returned as JSON.
DELETE Returns 204 No Content if the resource was deleted successfully.

Return values  https://docs.gitlab.com/ee/api/
Description
200 OK The GET, PUT or DELETE request was successful, the resource(s) itself is returned as JSON.
204 No Content The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.
201 Created The POST request was successful and the resource is returned as JSON.
304 Not Modified Indicates that the resource has not been modified since the last request.
400 Bad Request A required attribute of the API request is missing, e.g., the title of an issue is not given.
401 Unauthorized The user is not authenticated, a valid user token is necessary.
403 Forbidden The request is not allowed, e.g., the user is not allowed to delete a project.
404 Not Found A resource could not be accessed, e.g., an ID for a resource could not be found.
405 Method Not Allowed The request is not supported.
409 Conflict A conflicting resource already exists, e.g., creating a project with a name that already exists.
412 Indicates the request was denied. May happen if the If-Unmodified-Since header is provided when trying to delete a resource, which was modified in between.
422 Unprocessable The entity could not be processed.
500 Server Error While handling the request something went wrong server-side.



curl --header "PRIVATE-TOKEN: 9koXpg98eAheJpvBs5tK" --remote-header-name --remote-name https://gitlab.example.com/api/v4/projects/5/export/download
https://gitlab.com/api/v4/projects/8473228/export

curl -X POST http://gitlab.com/api/v4/session?login=v.uk@g.com&password=
curl -X POST http://gitlab.com/api/v4/projects?=private_token=xyz123

curl --header "Authorization: Bearer KQRU97zj3zyFhtyRsH5K" https://gitlab.com/api/v4/user
https://gitlab.com/api/v4/session --data 'login=v.uk@.com&password='

https://www.cambus.net/parsing-json-from-command-line-using-python/

http://10.112.78.16/api/v4/projects
https://gitlab.com/api/v4/users?private_token=uH7Cy7xoLV9_XnPDS9U8
http://10.112.78.16/api/v4/users?PRIVATE-TOKEN:wY-94pjQqM3yaMd

{"id":3264744,"web_url":"https://gitlab.com/groups/myhappy","name":" 778","path":"myhappy","description":"xianmg","visibility":"public","lfs_enabled":true,"avatar_url":null,"request_access_enabled":false,"full_name":" 778","full_path":"myhappy","parent_id":null,"ldap_cn":null,"ldap_access":null},
{"id":2958521,"web_url":"https://gitlab.com/groups/armagetronad-xtw","name":" Armagetron Advanced eXTreme World","path":"armagetronad-xtw","description":"Armagetron Advanced team, mainly to add and extend on features in specific branches.","visibility":"public","lfs_enabled":true,"avatar_url":null,"request_access_enabled":false,"full_name":" Armagetron Advanced eXTreme World","full_path":"armagetronad-xtw","parent_id":null,"ldap_cn":null,"ldap_access":null}

