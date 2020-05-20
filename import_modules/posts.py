from datetime import datetime as dt

def attrib_to_dict(attrib):
	result = {}

	result["_id"] = int(attrib.get("Id"))
	
	result["PostTypeId"] = int(attrib.get("PostTypeId"))
	
	# nullable attributes
	acceptedAnswerId = attrib.get("AcceptedAnswerId")
	if acceptedAnswerId: result["AcceptedAnswerId"] = int(acceptedAnswerId)
	
	parentId = attrib.get("ParentId")
	if parentId: result["ParentId"] = int(parentId)
	
	result["CreationDate"] = dt.fromisoformat(attrib.get("CreationDate"))
	
	result["Score"] = int(attrib.get("Score"))
	
	viewCount = attrib.get("ViewCount")
	if viewCount: result["ViewCount"] = int(viewCount)

	result["Body"] = attrib.get("Body")

	ownerUserId = attrib.get("OwnerUserId")
	if ownerUserId: result["OwnerUserId"] = int(ownerUserId)

	ownerDisplayName = attrib.get("OwnerDisplayName")
	if ownerDisplayName: result["OwnerDisplayName"] = ownerDisplayName

	lastEditorUserId = attrib.get("LastEditorUserId")
	if lastEditorUserId: result["LastEditorUserId"] = int(lastEditorUserId)

	lastEditorDisplayName = attrib.get("LastEditorDisplayName")
	if lastEditorDisplayName: result["LastEditorDisplayName"] = lastEditorDisplayName

	lastEditDate = attrib.get("LastEditDate")
	if lastEditDate: result["LastEditDate"] = dt.fromisoformat(lastEditDate)

	result["LastActivityDate"] = dt.fromisoformat(attrib.get("LastActivityDate"))
	
	title = attrib.get("Title")
	if title: result["Title"] = title

	tags = attrib.get("Tags")
	if tags: result["Tags"] = [tag[:-1] for tag in tags.split("<")[1:]]

	answerCount = attrib.get("AnswerCount")
	if answerCount: result["AnswerCount"] = int(answerCount)

	commentCount = attrib.get("CommentCount")
	if commentCount: result["CommentCount"] = int(commentCount)

	favoriteCount = attrib.get("FavoriteCount")
	if favoriteCount: result["FavoriteCount"] = int(favoriteCount)

	closedDate = attrib.get("ClosedDate")
	if closedDate: result["ClosedDate"] = dt.fromisoformat(closedDate)

	communityOwnedDate = attrib.get("CommunityOwnedDate")
	if communityOwnedDate: result["CommunityOwnedDate"] = dt.fromisoformat(communityOwnedDate)

	return result
