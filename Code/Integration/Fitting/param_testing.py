def runner(setup, dataset):
    # Unpack the algorithm and parameters from the setup
    algorithm_class = setup['algorithm']
    params = setup['params']

    # Instantiate the Algorithm class with the provided parameters
    algorithm_instance = algorithm_class(*params)

    # Run the algorithm on the provided dataset and return the results
    results = algorithm_instance.run(dataset)

    return results

