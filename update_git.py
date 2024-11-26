import subprocess

def commit_and_push(file_name, commit_message, branch_name="main"):
    try:
        subprocess.run(["git", "add", file_name], check=True)
        
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        subprocess.run(["git", "push", "origin", branch_name], check=True)
        
        print(f"File '{file_name}' committato e pushato su GitHub con successo!")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante il processo Git: {e}")

branch_name = "main" 
commit_message = "update csv file"
csv_file = 'finbert_aapl.csv'

commit_and_push(csv_file, commit_message, branch_name)


branch_name = "main" 
commit_message = "update csv file"
csv_file = 'prices.csv'

commit_and_push(csv_file, commit_message, branch_name)