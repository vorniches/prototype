# Prototype – Django + OpenAI Quick Start Project

This is a quick-start template for setting up a **Django** project with **OpenAI integration**. The project is containerized with Docker, allowing for easy setup and consistent deployment.

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