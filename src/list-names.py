import argparse


def main():
    argparser = argparse.ArgumentParser(
        description="Extract the names from a simple-fastq file")
    argparser.add_argument(
        "fastq",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    #print(f"Now I need to process the records in {args.fastq}")
    lines = args.fastq.readlines()
    for line in lines[0:len(lines):2]:
        print(line.replace("\n", "").replace("@", "", 1))



if __name__ == '__main__':
    main()
