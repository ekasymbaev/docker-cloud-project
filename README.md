
Project 3 — Docker (End-to-End Container + Kubernetes Extra Credit)

This project builds a lightweight Docker image that automatically:
	•	reads two text files inside the container
	•	computes word statistics
	•	detects the container’s IP address
	•	writes results to /home/data/output/result.txt
	•	prints the contents of result.txt to the console and exits

Extra credit: deploys two replicas using Kubernetes (Docker Desktop) and captures pod status output.

⸻

✅ Requirements Covered

Docker Container
	•	Uses a lightweight base image (python:3-alpine)
	•	Reads:
	•	/home/data/IF.txt
	•	/home/data/AlwaysRememberUsThisWay.txt
	•	Outputs:
	•	total words in each file
	•	grand total words
	•	top 3 frequent words in IF.txt
	•	top 3 frequent words in AlwaysRememberUsThisWay.txt after splitting contractions
	•	container IP address
	•	Writes results to:
/home/data/output/result.txt
	•	Prints result.txt to console when the container runs

⸻

📁 Project Structure

docker_project3/
│
├── Dockerfile
├── deployment.yaml              # (extra credit)
├── kube_output.txt              # (extra credit output)
├── kasymbet.tar                 # exported image (for submission)
│
├── data/
│   ├── IF.txt
│   └── AlwaysRememberUsThisWay.txt
│
└── scripts/
    └── script.py


⸻

🐳 Docker Instructions

1) Build the image

From inside the docker_project3 folder:

docker build -t project3-image .


⸻

2) Run the container

docker run --rm project3-image

This will:
	•	execute script.py
	•	generate /home/data/output/result.txt
	•	print the contents to the console
	•	exit automatically

⸻

3) Save the image as a .tar (for submission)

docker save -o kasymbet.tar project3-image


⸻

4) Load and run from .tar (grader workflow)

docker load -i kasymbet.tar
docker run --rm project3-image


⸻

⭐ Extra Credit — Kubernetes (Docker Desktop)

1) Enable Kubernetes

Docker Desktop → Settings → Kubernetes → Enable Kubernetes

Verify:

kubectl get nodes


⸻

2) Deploy 2 replicas

kubectl apply -f deployment.yaml
kubectl get pods
kubectl get deploy

You should see 2 running pods.

⸻

3) Save pod status output

kubectl get pods > kube_output.txt
cat kube_output.txt


⸻

4) View logs from replicas

kubectl logs -l app=project3 --tail=50


⸻

5) Cleanup

kubectl delete -f deployment.yaml


⸻

📝 Notes
	•	Contractions are handled by splitting apostrophes (e.g., don't → don t, I'm → I m).
	•	IP addresses may differ between Docker standalone runs and Kubernetes runs (this is normal).
	•	The image size is approximately 76MB, which is well below the required 200MB target.

⸻

If you want, I can now:
	•	🔹 Make it even more professional (A-level polished)
	•	🔹 Or simplify it to look more like your friend’s exact format
	•	🔹 Or format it in perfect GitHub Markdown styling

Tell me which version you want.