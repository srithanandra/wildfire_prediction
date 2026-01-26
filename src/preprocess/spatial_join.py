import numpy as np
from sklearn.neighbors import BallTree

def spatial_match(base, ref, radius_km):
    base_coords = np.radians(base[['latitude', 'longitude']])
    ref_coords = np.radians(ref[['latitude', 'longitude']])
    tree = BallTree(ref_coords, metric='haversine')
    ind = tree.query_radius(base_coords, r=radius_km / 6371)
    return np.array([len(i) > 0 for i in ind])
