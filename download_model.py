from urllib.request import urlretrieve

def main():

    url = 'https://www.dropbox.com/scl/fi/ngwvakmytc0rzy6k43taz/model.h5?rlkey=q4hg17kj90q57xm1uixwav45c&dl=1'
    filename = 'models/model.h5'

    urlretrieve(url, filename)

if __name__=='__main__':
    main()