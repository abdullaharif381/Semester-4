from mrjob.job import MRJob

# define the mapper class
class MRJob_Songs(MRJob):

    
    def mapper(self, _, line):
        # split the line by comma
        fields = line.split(",")
       
        username = fields[0]
        songs = fields[2:]
        
        if len(songs) > 5:
         
            yield username, len(songs)

# run the job
if __name__ == "__main__":
    MRJob_Songs.run()
