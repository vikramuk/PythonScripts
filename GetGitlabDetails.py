import gitlab, os, sys
import logging
import requests, json, time,urllib
from requests.models import PreparedRequest
#https://stackoverflow.com/questions/2506379/add-params-to-given-url-in-python

headers = {
    'PRIVATE_TOKEN': '',
}

param2 = (
    ('private_token', ''),
    ('statistics', 'true'),
)


def GetDetails(projectid):
	prjID=projectid #.rstrip('\n')
	print (prjID)
	getProjectBranches(prjID)
	getProjectCommits(prjID)
	getProjectStatistics(prjID)
	
def getProjectBranches(prjID):
	#print ("Am in Branch")
	URL='https://gitlab.com/api/v4/projects/'+prjID+'/repository/branches'
	r = requests.get(URL, headers=headers)
	#print (URL)
	data = r.json()
	if (r.status_code==200):
		#print(r.headers)
		#print(r.headers['content-type'])
		data = r.json()
		#print (data)
		print (data[0]['name'])
		#BranchName=data["name"]
		'''
		BranchID=data['commit']['id']
		BranchCommiter=data['commit']['committer_name']
		print("BranchID:%s\n BranchCommiter:%s" %(BranchID,BranchCommiter))
		time.sleep(2)
		print (data['name'])
		print(data['commit'])
		'''

def getProjectCommits(prjID):
	#print ("Am in Commits")
	URL='https://gitlab.com/api/v4/projects/'+prjID+'/repository/commits'
	r = requests.get(URL, headers=headers)
	#print (URL)
	data = r.json()
	if (r.status_code == 200):
		#print(r.headers)
		data = r.json()
		#print (data)
		#print (data[0][0]['short_id'])
		CommitID=data[0]['id']
		shortID=data[0]['short_id']
		Commiter=data[0]['committer_name']
		print("BranchName:%s\n BranchID:%s\n BranchCommiter:%s" %(CommitID, shortID,Commiter))
		'''
		time.sleep(2)
		print (data['id'])
		print(data['short_id'])
		'''
	
def getProjectStatistics(prjID):
	#print ("Am in Statistics")
	URL='https://gitlab.com/api/v4/projects/'+prjID
	r = requests.get(URL, params=param2)
	data = r.json()
	#print (data)
	if (r.status_code == 200):
		data = r.json()
		IssueCount=data['open_issues_count']
		CommitCount=data['statistics']['commit_count']
		Filesize=data['statistics']['storage_size']
		Reposize=data['statistics']['repository_size']
		print("IssueCount:%s\n Commits:%s \n FileSize:%s\n RepoSize:%s" %(IssueCount,CommitCount, Filesize,Reposize))
	
def GetProjectDetails():

	'''
	filepath = "C:\\Users\\vikram.uk\\Desktop\\ProjectList.txt" 
	with open(filepath) as fp:  
	   for cnt, line in enumerate(fp):
		   print("Line {}: {}".format(cnt, line))	
	   '''
	try:	
		ProjectFile = open("C:\\Users\\vikram.uk\\Desktop\\ProjectList.txt", "r")	
		with open("C:\\Users\\vikram.uk\\Desktop\\ProjectList.txt") as f:
			content = f.read().splitlines()
			print (content)			
	except:
		print("List of Projects is Empty")
		exit(0)	
	for projectid in content:
					GetDetails(projectid)
					#print (projectid)
					
if __name__ =="__main__":
	#Gitlab = gitlab.Gitlab.from_config('Gitlab', ['C:\\Users\\vikram.uk\\Desktop\\python-gitlab.cfg'])
	GetProjectDetails()
