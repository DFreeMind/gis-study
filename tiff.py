import rasterio

dataset = rasterio.open("/Users/luqiu/Downloads/96.tif")
bounds = dataset.bounds
print("范围:", bounds)
print("波段数量:", dataset.count)
print("宽/高:", dataset.width, dataset.height)
print(bounds.right - bounds.left)