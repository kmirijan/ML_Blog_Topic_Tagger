import os, re, json

def setup_json(file_name):
	new_dict = {'pid':'', 'sex':'', 'age':'', 'industry':'', 'sign':'', 'posts':{}}
	split = file_name.split('.')

	new_dict['pid'] = split[0]
	new_dict['sex'] = split[1]
	new_dict['age'] = split[2]
	new_dict['industry'] = split[3]
	new_dict['sign'] = split[4]

	return new_dict

def clean_text(line):
	s = line
	s = s.lower()
	s = s.replace('&nbsp;', " ")
	s = s.replace('&nbsp', " ")
	s = s.replace('&amp;', '&')
	s = s.replace('&amp', '&')
	s = s.replace('&quot;', '\"')
	s = s.replace('&quot', '\"')
	s = s.replace('&apos;', '\'')
	s = s.replace('&apos', '\'')
	s = s.replace('&lt;', '<')
	s = s.replace('&lt', '<')
	s = s.replace('&gt;', '>')
	s = s.replace('&gt', '>')
	s = s.replace('urllink', '')

	return s

def reform_xml(has_industry):
	for file_name in has_industry:
		new_dict = setup_json(file_name)

		path = 'blogs/' + file_name
		my_file = open(path, 'r', errors='ignore')
		lines = my_file.readlines()
		print(file_name)
		postID = 0
		for i in range(len(lines)):
			if '<date>' in lines[i]:
				date = re.search('<date>(.*)</date>', lines[i])

				s = clean_text(lines[i+4])
				new_dict['posts'][postID] = {'date':date.group(1), 'text':s, 'gold_tags':None, 'model_tags':None}
				postID += 1

				i += 4

		json_file_name = file_name[:-3] + 'json'
		with open('json_blogs/' + json_file_name, 'w') as fp:
			json.dump(new_dict, fp)

def main():
	arr = os.listdir('blogs')
	has_industry = []
	# no_industry = []
	industries = set()

	for file_name in arr:
		split = file_name.split('.')

		if split[3] != 'indUnk':
			industries.add(split[3])
			has_industry.append(file_name)

	reform_xml(has_industry)

if __name__ == '__main__':
    main()