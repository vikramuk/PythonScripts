import gitlab, os, sys
import logging
import requests, json, time

headers = {
    'PRIVATE_TOKEN': '',
}

def GetDetails(projectid):
	prjID=projectid #.rstrip('\n')
	print (prjID)
	getProjectBranches(prjID)
	getProjectCommits(prjID)
	
def getProjectBranches(prjID):
	print ("Am in Branch")
	URL='https://gitlab.com/api/v4/projects/'+prjID+'/repository/branches'
	r = requests.get(URL, headers=headers)
	#print (URL)
	data = r.json()
	if (r.status_code==200):
		#print(r.headers)
		#print(r.headers['content-type'])
		#print(r.json())
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
	print ("Am in Commits")
	URL='https://gitlab.com/api/v4/projects/'+prjID+'/repository/commits'
	r = requests.get(URL, headers=headers)
	#print (URL)
	data = r.json()
	if (r.status_code == 200):
		#print(r.headers)
		#print(r.headers['content-type'])
		#print(r.json())
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
	
def getProjectStatistics():
	print ("Am in Statistics")
	pass
	
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
					print (projectid)
					
if __name__ =="__main__":
	#Gitlab = gitlab.Gitlab.from_config('Gitlab', ['C:\\Users\\vikram.uk\\Desktop\\python-gitlab.cfg'])
	GetProjectDetails()
