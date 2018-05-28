#docker run --rm -it -v `pwd`/gitlab-runner:/etc/gitlab-runner --name gitlab-runner gitlab/gitlab-runner
docker run -d -v `pwd`/gitlab-runner:/etc/gitlab-runner  -v /var/run/docker.sock:/var/run/docker.sock --restart always --name gitlab-runner gitlab/gitlab-runner
