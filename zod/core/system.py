import subprocess
import json


class system:
    def run_command(self, command: str):
        try:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            status_code = result.returncode
            output = result.stdout.strip()
            response_data = {"data": output, "code": str(status_code)}
            json_data = json.dumps(response_data)
            return json_data

        except subprocess.CalledProcessError as e:
            error_data = {"data": e.stderr.strip(), "code": str(e.returncode)}
            json_error = json.dumps(error_data)
            return json_error

    def reload_app(self, name, signal):
        try:
            self.run_command(f"pkill -{signal} {name}")
            # subprocess.run(["pkill", f"-{signal}", name], check=True)
        except subprocess.CalledProcessError as e:
            raise (e)
        return True
