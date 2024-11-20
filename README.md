# localstack

## Usage
```
docker-compose up -d
```

## install awscli-local
```
pip install awscli-local
```

## Create buckets

```
aws --endpoint-url=http://localhost:4566 s3api create-bucket --bucket my-test-bucket
```
