# Prototype

This is a quick-start template for setting up a **Django** project with **OpenAI integration**. The project is containerized with Docker, allowing for easy setup and consistent deployment.

> Check out the report on creating with Prototype on [dev.to](https://dev.to/vorniches/building-self-hosted-telegraph-in-1-prompt-and-3-minutes-2li2) or [YouTube](https://youtu.be/ArPGGaG5EU8).

## Shoutouts

Prototype was featured as a top project on Product Hunt.

<div align="center">
  <a href="https://www.producthunt.com/posts/prototype?embed=true&utm_source=badge-top-post-topic-badge&utm_medium=badge&utm_souce=badge-prototype" target="_blank">
    <img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-topic-badge.svg?post_id=864287&theme=dark&period=weekly&topic_id=237&t=1739886900372" 
    alt="Prototype - Product Hunt" width="250" height="54" />
  </a>
  <a href="https://www.producthunt.com/posts/prototype?embed=true&utm_source=badge-top-post-badge&utm_medium=badge&utm_souce=badge-prototype" target="_blank">
    <img src="https://api.producthunt.com/widgets/embed-image/v1/top-post-badge.svg?post_id=864287&theme=dark&period=daily&t=1739439944508" 
    alt="Prototype - Product Hunt" width="250" height="54" />
  </a>
</div>

## Requirements

Before starting, ensure you have:

- **Docker** and **Docker Compose** installed (latest versions recommended).

## Quick Start

### Step 1: Clone the repository

```bash
git clone https://github.com/vorniches/prototype your_app_name
cd your_app_name
```

### Step 2: Start the project

Run the following command to set up the environment:

```bash
./setup.sh
```

This will:

1. Create a Django project (if not already present).
2. Move the `openai_helper.py` to the appropriate directory.
3. Build and start the Docker containers.

## Access the Application

The Django development server will be available at:

- [http://localhost:9009](http://localhost:9009)

## Configuration

### Environment Variables

1. Copy the `example.env` file to `.env`:

   ```bash
   cp example.env .env
   ```

2. Edit `.env` to include your OpenAI API key:

   ```bash
   OPENAI_API_KEY=<your_openai_api_key>
   ```

3. Ensure the environment variables are loaded into Django's `settings.py`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
