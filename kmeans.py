import time
import numpy as np
from sklearn.datasets import make_blobs

def generateData(n, c):
  X, y = make_blobs(n_samples=n, centers=c, cluster_std=1.7, shuffle=False, random_state=2122)
  return X

def nearestCentroid(datum, centroids):
  dist = np.linalg.norm(centroids - datum, axis=1)
  return np.argmin(dist), np.min(dist)

def kmeans(k, data, nr_iter=100):
  N = len(data)
  centroids = data[np.random.choice(np.array(range(N)), size=k, replace=False)]
  c = np.zeros(N, dtype=int)

  total_variation = 0.0
  assignment_time = 0.0
  update_time = 0.0

  for j in range(nr_iter):
      # Timing the assignment step
      start_assignment = time.time()
      variation = np.zeros(k)
      cluster_sizes = np.zeros(k, dtype=int)
      cluster_assignments = {x: [] for x in range(k)}
      for i in range(N):
          cluster, dist = nearestCentroid(data[i], centroids)
          c[i] = cluster
          cluster_assignments[cluster].append(data[i])
          cluster_sizes[cluster] += 1
          variation[cluster] += dist**2
      end_assignment = time.time()
      assignment_time += (end_assignment - start_assignment)

      # Timing the update step
      start_update = time.time()
      centroids = np.zeros((k, 2))
      for i in range(N):
          centroids[c[i]] += data[i]
      centroids = centroids / cluster_sizes.reshape(-1, 1)
      end_update = time.time()
      update_time += (end_update - start_update)

  return total_variation, c, assignment_time, update_time

# Example usage
X = generateData(10000, 4)
start_time = time.time()
total_variation, assignment, assignment_time, update_time = kmeans(4, X, nr_iter=100)
end_time = time.time()

total_time = end_time - start_time
print(f"Total execution time: {total_time:.4f}s")
print(f"Assignment step time: {assignment_time:.4f}s ({assignment_time/total_time:.2%} of total)")
print(f"Update step time: {update_time:.4f}s ({update_time/total_time:.2%} of total)")