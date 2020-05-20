def attrib_to_dict(attrib):
	result = {}
	
	result["_id"] = int(attrib.get("Id"))
	result["TagName"] = attrib.get("TagName")
	result["Count"] = int(attrib.get("Count"))
	
	excerptPostId = attrib.get("ExcerptPostId")
	if excerptPostId: result["ExcerptPostId"] = int(excerptPostId)
	
	wikiPostId = attrib.get("WikiPostId")
	if wikiPostId: result["WikiPostId"] = int(wikiPostId)
	
	return result
