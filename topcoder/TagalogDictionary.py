class TagalogDictionary:
	def sortWords(self, words):
		a = list(words)
		a.sort(key = ["C", "B", "A"])
		return tuple(a)

p = TagalogDictionary()
print p.sortWords({"knilngiggnngginggn","ingkigningg","kingkong","dingdong","dindong","dingdont","ingkblot"})
