# small_test_ops
test_for_my_ops

docker build -t IMAGE .
docker tag SOURCE_IMAGE HOSTNAME/PROJECT-ID/IMAGE:TAG

docker login -u _json_key --password-stdin https://eu.gcr.io < credentinals.json

docker push SOURCE_IMAGE HOSTNAME/PROJECT-ID/IMAGE:TAG
