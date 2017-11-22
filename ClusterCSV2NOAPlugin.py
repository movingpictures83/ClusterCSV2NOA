import sys

class ClusterCSV2NOAPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      csvfile = open(self.myfile, 'r')
      self.clusters = []
      for line in csvfile:
         contents = line.split(',')
         if (len(contents[0]) == 2):  # Two quotes
            self.clusters.append([])
         else:
            name = contents[1].strip()
            name = name[1:len(name)-1]
            self.clusters[len(self.clusters)-1].append(name)


   def output(self, filename):
      noafile = open(filename, 'w')
      noafile.write("Name"+"\t"+"Cluster"+"\n")

      i = 1
      for cluster in self.clusters:
         if (len(cluster) == 1):   # A singleton should count as cluster 0 for coloring
            noafile.write(cluster[0]+"\t"+str(0)+"\n")
         else:
            for node in cluster:
               noafile.write(node+"\t"+str(i)+"\n")
         i += 1







