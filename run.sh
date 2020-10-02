helm repo add influxdata https://helm.influxdata.com/
helm upgrade --install chronograf --\
	influxdata/chronograf \
	--set persistence.storageClass=db-sc