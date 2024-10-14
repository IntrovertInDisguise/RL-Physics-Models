# RL-Physics-Models
Testing different learning methods to control physics models

Web page: https://introvertindisguise.github.io/RL-Physics-Models/



## Setting up the Environment

To recreate the environment, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/introvertindisguise/RL-Physics-Models.git
    cd RL-Physics-Models
    ```

2. Create and activate the Conda environment:
    ```bash
    conda create --prefix ./CondaEnvs/LearnEnv python=3.11
    conda activate ./CondaEnvs/LearnEnv
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Start Jupyter Notebook:
    ```bash
    jupyter notebook
    ```

If you face any installation issues, ensure that CUDA drivers are properly installed for GPU support.
