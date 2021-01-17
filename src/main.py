import sample_pb2
import sys

output = sample_pb2.Sample()
output.field_one = "test"
output.field_two = 999

print("output to sample.bin")

f = open("sample.bin", "wb")
f.write(output.SerializeToString())
f.close

print("input from sample.bin")

f = open("sample.bin", "rb")
input = sample_pb2.Sample()
input.ParseFromString(f.read())
f.close()

print("output")
print(input)
