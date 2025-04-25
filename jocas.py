import os
import s3fs
import pandas as pd

fs = s3fs.S3FileSystem(
    key=os.environ["AWS_ACCESS_KEY_ID"],
    secret=os.environ["AWS_SECRET_ACCESS_KEY"],
    token=os.environ["AWS_SESSION_TOKEN"],
    client_kwargs={"endpoint_url": "https://minio.lab.sspcloud.fr"}
)

df = pd.read_parquet(
    'projet-jocas-prod/diffusion/JOCAS/annee=2022/mois=12/20221231_offers_0.parquet',
    filesystem=fs
)

df.to_csv('/Users/caroline/Downloads/jocas_2022_12.csv', index=False)

