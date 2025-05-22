# ECS

[Excalidraw link](https://link.excalidraw.com/l/6gPaBlSh8PG/3saNZRry8wV)

## Building an image for ECR

1. Make the ECR repository
2. Get the ECR repository's push commands
3. Run the first command (login)
4. Run a **modified** second command:
    - `docker build -t [name of repo] --platform=linux/amd64 --provenance=false .`
        - Build the image
        - With the same name as the repo
        - Aiming for Linux environment when running it
        - Not sending a lot of metadata
3. Run the third command (tag)
4. Run the fourth command (push)