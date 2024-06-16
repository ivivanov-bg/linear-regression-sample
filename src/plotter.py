import matplotlib.pyplot as plt
from scipy import stats

if __name__ == "__main__":
  plot()

def read_data(filepath):
  file = open(filepath, 'r')
  lines = file.read().splitlines()
  
  data = list(map(lambda r: r.split(";"), lines))

  return data

def plot():
  print("Sample main start")
  
  data = read_data("data/linear.txt")
  print(data)
  
#  x = list(map(lambda d: d[0], data))
#  y = list(map(lambda d: d[1], data))

  x = [ 5, 7, 8, 7, 2,17, 2, 9, 4,11, 12,  9,  6]
  y = [99,85,83,80,67,70,77,83,89,92,105,109,114]

  slope, intercept, r, p, std_err = stats.linregress(x, y)
  
  def myfunc(x):
    return slope * x + intercept

  mymodel = list(map(myfunc, x))
  
  plt.scatter(x, y)
  plt.plot(x, mymodel)
  plt.savefig("out.png")
  
  print("Sample main end")
