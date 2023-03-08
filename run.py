import subprocess

# Ask how many times to run the script
num_runs = int(input("Enter number of times to run the script: "))

for i in range(num_runs):
    # Run step1.py and print status
    print(f"Running step1 Generating Story for run {i+1}...")
    result = subprocess.run(["python3", "step1.py"])
    if result.returncode == 0:
        print("Step 1 complete.")
    else:
        print("Step 1 failed.")
        continue

    # Run step2.py and print status
    print(f"Running step2 Generating Audio for run {i+1}...")
    result = subprocess.run(["python3", "step2.py"])
    if result.returncode == 0:
        print("Step 2 complete.")
    else:
        print("Step 2 failed.")
        continue

    # Run step3.py and print status
    print(f"Running step3 Generating Images for run {i+1}...")
    while True:
        result = subprocess.run(["python3", "step3.py"])
        if result.returncode == 0:
            print("Step 3 complete.")
            break
        elif result.returncode == 1:
            print("Error in step3.py. Starting over from step1.py...")
            break
        else:
            print("Step 3 failed. Trying again...")
            continue

    # Run step4.py and print status
    print(f"Running step4 Generating Video for run {i+1}...")
    result = subprocess.run(["python3", "step4.py"])
    if result.returncode == 0:
        print("Step 4 complete.")
    else:
        print("Step 4 failed.")
        continue

    # Run step5.py and print status
    print(f"Running step5 Cleaning up and archiving temporary files {i+1}...")
    result = subprocess.run(["python3", "step5.py"])
    if result.returncode == 0:
        print("Step 5 complete.")
    else:
        print("Step 5 complete-ish.")
        continue

 #TODO step6 wrestle stupid youtube oauth or upload straight to tiktok or instagram, which may be an even worse nightmare.

print("All runs complete.")
