# ML-devops_integration_project

Task Overview:
1. Create a container image that has Python3 and Keras or numpy installed using dockerfile.

2. When we launch this image, it should automatically starts train the model in the container.

3. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 

4. Job1 : Pull the Github repo automatically when some developers push repo to Github.

5. Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the software required for the CNN processing).

6. Job3 : Train your model and predict accuracy or metrics. If metrics accuracy is less than 80%, then tweak the machine learning model architecture. Retrain the model and get the train model.

7. Job4: This job sent the notification to developer.

9. Create One extra job job5 for monitor : If container, where app is running, fails due to any reason then this job should automatically start the container again. And also sent a mail to developer.
