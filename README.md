# SLIVER: Streamlined Lightweight Infrastructure for Vulnerability Exploration & Research
Forked from elkninja's [Elastic Stack Docker Part 1](https://github.com/elkninja/elastic-stack-docker-part-one)</sub>

## Introduction

**Sliver** is a lightweight Docker-based environment designed for researchers to explore vulnerabilities and conduct security research in a controlled, minimalistic setup. By leveraging Docker Compose and a simplified ELK stack, Sliver provides an easily deployable, streamlined infrastructure for vulnerability analysis, without the overhead of a full-scale security solution. A lighthearted play on words, Sliver is "Security Onion Lite".

## Project Goals

- Provide a minimal, scalable environment for vulnerability research.
- Offer a simple, lightweight setup with essential tools for exploration.
- Enable researchers to:
  - Test security tools in real-time.
  - Simulate basic environments for vulnerability exploration.
  - Analyze potential exploits in a controlled lab setting.

## Benefits

- **Lightweight:** Minimal resource requirements, designed for quick deployment and testing.
- **Flexible:** Easily adaptable for specific research tools and needs.
- **Portable:** Docker-compose allows for fast setup and teardown, enabling experimentation across various environments.
- **Focused on Research:** Designed to assist in vulnerability exploration without the distractions of unnecessary tools.

## Getting Started

This repository contains a Docker Compose file and associated configurations to quickly spin up a lightweight ELK stack environment for research purposes. This compose file hosts a Zeek container for processing
packet capture files (PCAP) as well as a jupyter notebook ready-to-go for analysts of all experience levels to begin exploring. 

## Prerequisites

- Familiarity with Docker and Docker Compose.
- Basic understanding of ELK stack components (Elasticsearch, Logstash, Kibana).
- Ability to configure and extend the setup for custom research needs.

## Setup Instructions

1. Clone the repository:  
   `git clone https://github.com/yourusername/sliver.git`

2. Navigate to the project directory:  
   `cd sliver`
   
3. Add Packet Capture files into the /pcap directory
   
4. Start the environment using Docker Compose:  
   `docker compose up -d`
5. Begin processing data or configuring the stack to suit your research purposes.
    - 5a. Console into the zeek container: `docker compose exec -it zeek01 /bin/bash`
    - 5b. Change into (logstash or filebeat) directory: `cd logstash_data_ingest/`
    - 5c. Run zeek against the pcap `zeek -Cr /pcap/sample.pcap`
      
6. Access Kibana or Jupyter Notebook through your browser:  
  - Kibana: `http://localhost:5601`
  - Jupyter: `http://localhost:8888/<i>token</i>`
    
<i>Helpful tip:</i> Performing a 'watch' on the container processes can help to identify container's status' and aid in troubleshooting

i.e: `watch 'docker compose ps'`

## Additional Tools

Sliver includes basic ELK stack components but can be extended with additional tools as needed for specific vulnerability research tasks.

## Documentation

For more details on ELK and Docker, refer to the official documentation:

- Docker: [https://docs.docker.com/](https://docs.docker.com/)
- ELK Stack: [https://www.elastic.co/what-is/elk-stack](https://www.elastic.co/what-is/elk-stack)

## Contributing

Contributions to Sliver are welcome! If you have improvements, bug fixes, or additional tools to suggest, feel free to submit a pull request.

## Disclaimer

Sliver is intended for educational and research purposes only. Please use responsibly and in accordance with applicable laws and regulations.
