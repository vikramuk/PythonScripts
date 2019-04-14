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
	getProjectStatistics(prjID)
	getProjectBranches(prjID)
	getProjectCommits(prjID)
		
def getProjectBranches(prjID):
	#print ("Am in Branch")
	URL='https://gitlab.com/api/v4/projects/'+prjID+'/repository/branches'
	r = requests.get(URL, headers=headers)
	#print (URL)
	data = r.json()
	if (r.status_code==200):
		data = r.json()
		print (data[0]['name'],data[0]['commit']['id'])
		for branches in data:			
			BranchName =branches['name']
			BranchID = branches['commit']['short_id']
			CommitterEmail = branches['commit']['committer_email']
			print("BranchName:%s\t BranchID:%s\t BranchCommitter:%s " %(BranchName, BranchID,CommitterEmail))
			
def getProjectCommits(prjID):
	#print ("Am in Commits")
	URL='https://gitlab.com/api/v4/projects/'+prjID+'/repository/commits'
	r = requests.get(URL, headers=headers)
	data = r.json()
	if (r.status_code == 200):
		CommitID=data[0]['id']
		shortID=data[0]['short_id']
		Commiter=data[0]['committer_name']
		print("CommitName:%s\t CommitID:%s\t Commiter:%s \n" %(CommitID, shortID,Commiter))
		for commit in data:			
			commmitName =commit['id']
			commitID = commit['short_id']
			CommitterEmail = commit['committer_email']
			print("CommitName:%s\t CommitID:%s\t CommitCommitter:%s " %(commmitName, commitID,CommitterEmail))
			
def getProjectStatistics(prjID):
	#print ("Am in Statistics")
	URL='https://gitlab.com/api/v4/projects/'+prjID
	r = requests.get(URL, params=param2)
	data = r.json()
	if (r.status_code == 200):
		data = r.json()
		ProjectID =prjID
		ProjectName =data['name']
		ProjectNameSpace=data['name_with_namespace']
		DefBranch=data['default_branch']
		SSHRepo=data['ssh_url_to_repo']
		IssueCount=data['open_issues_count']
		CommitCount=data['statistics']['commit_count']
		Filesize=data['statistics']['storage_size']
		Reposize=data['statistics']['repository_size']
		print("ProjectID: %s \t ProjectName %s \t ProjectNameSpace %s \t DefBranch %s \t SSHRepo %s \t IssueCount:%s \t Commits:%s \t FileSize:%s\t RepoSize:%s \n" %(ProjectID,ProjectName,ProjectNameSpace,DefBranch,SSHRepo,IssueCount,CommitCount, Filesize,Reposize))
	
def GetProjectDetails():
	try:	
		ProjectFile = open("C:\\Users\\vikram.uk\\Desktop\\ProjectList.txt", "r")	
		with open("C:\\Users\\vikram.uk\\Desktop\\ProjectList.txt") as f:
			content = f.read().splitlines()
			#print (content)			
	except:
		print("List of Projects is Empty")
		exit(0)	
	for projectid in content:
					GetDetails(projectid)
					#print (projectid)
					
if __name__ =="__main__":
	GetProjectDetails()
