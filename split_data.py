import os, random, shutil

DATAPATH = 'json_blogs/'

def copy_files(filenames, dir_name):
	for filename in filenames:
		shutil.copy(DATAPATH + filename, 'json_splits/' + dir_name)

def main():
	filenames = os.listdir(DATAPATH)
	filenames.sort()
	random.seed(200)
	random.shuffle(filenames)

	split_1 = int(.8 * len(filenames))
	split_2 = int(.9 * len(filenames))
	train_filenames = filenames[:split_1]
	dev_filenames = filenames[split_1:split_2]
	test_filenames = filenames[split_2:]

	copy_files(train_filenames, 'train/')
	copy_files(dev_filenames, 'dev/')
	copy_files(test_filenames, 'test/')

if __name__ == '__main__':
    main()