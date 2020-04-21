from pyterum.fragmenter import FragmenterInput, FragmenterOutput
from pyterum import env


if __name__ == "__main__":
    fragmenter_in = FragmenterInput(env.EXAMPLE_SOCKET_INPUT)
    fragmenter_out = FragmenterOutput(env.EXAMPLE_SOCKET_OUTPUT)

    for file_list in fragmenter_in.consumer():
        print(f"received: {file_list}", flush=True)
        for f in file_list:
            msg = [f]
            print(f"sending: {msg}", flush=True)
            fragmenter_out.produce(msg)