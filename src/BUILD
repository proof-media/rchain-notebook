python_library(
  name="rchain_grpc",
  dependencies=[
    "src/python/3rdparty/python:grpcio-tools",
    "src/python/3rdparty/python:googleapis-common-protos",
    ":proto"
  ],
  sources=rglobs("*.py"),
  provides=setup_py(
    name='rchain_grpc',
    version='0.0.1',
    description='Client libilary for rchain gRPC interface',
    license='Apache License, Version 2.0',
    zip_safe=True,
    classifiers=[
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Apache Software License',
      'Operating System :: POSIX :: Linux',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3 :: Only'
    ]
  )
)

files(
  name="proto",
  sources=rglobs("*.proto")
)
