import numpy
import ga
import client_moodle

"""
The y=target is to maximize this equation ASAP:
    y = w1x1+w2x2+w3x3+w4x4+w5x5+6wx6
    where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7)
    What are the best values for the 6 weights w1 to w6?
    We are going to use the genetic algorithm for the best possible values after a number of generations.
"""



# Number of the weights we are looking to optimize.
num_weights = 11
overfit_wt = [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
"""
Genetic algorithm parameters:
    Mating pool size
    Population size
"""
sol_per_pop = 8
num_parents_mating = 6
num_children_to_take = 6
num_parents_to_take = 2


# Defining the population size.
pop_size = (sol_per_pop,num_weights) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.

new_population = numpy.random.uniform(low=-10.0, high=10.0, size=pop_size)



for i in range(11):
    new_population[0,i] = overfit_wt[i]








print("this is the new population when overfit guy is just added", new_population.tolist())

num_generations = 10

for generation in range(num_generations):
    print("Generation : ", generation)
   
    # Measing the fitness of each chromosome in the population.
    
    fitness = ga.cal_pop_fitness(new_population)

    # Selecting the best parents in the population for mating.
    parents = ga.select_mating_pool(new_population, fitness, 
                                      num_parents_mating)

    print("Parents allowed to mate in this generation: ", parents)

    # Generating next generation using crossover.
    # offspring_crossover = ga.crossover(parents,
    #                                    offspring_size=(pop_size[0]-parents.shape[0], num_weights))
    offspring_crossover = ga.crossover(parents,
                                       offspring_size=(num_children_to_take, num_weights))

    print("offsprings crossover length:", len(offspring_crossover))
    print("offspring crossover is as follows -",offspring_crossover)
    # Adding some variations to the offsrping using mutation.
    offspring_mutation = ga.mutation(offspring_crossover)
    print("Offspring_mutation is as follows - ", offspring_mutation)

    # Creating the new population based on the parents and offspring.
    # new_population[0:parents.shape[0], :] = parents
    # new_population[parents.shape[0]:, :] = offspring_mutation
    
    new_population = ga.create_new_pop(parents,offspring_mutation,num_parents_to_take,num_children_to_take)
    
    
    
    # The best result in the current iteration.
    # print("Best result : ", numpy.max(numpy.sum(new_population*equation_inputs, axis=1)))

# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
print("final:",new_population.tolist())

print("final fitness:",fitness)
# print(fitness)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.min(fitness))
print("best match!", best_match_idx)
# print("Best_match_index:", best_match_idx)
ans = list(new_population[best_match_idx, :][0  ][0])
# ans = list(new_population[best_match_idx])
print("Best solution : ", ans )
# print("Best solution fitness : ", list(fitness[best_match_idx]))

p=list(client_moodle.get_errors('bTcDQRvCITniLCqT38zzd4CaYs8gPsrnjxyZyIVTiTv6DyX0kX',list(new_population[best_match_idx, :][0  ][0]) ))
print("Best solution fitness : ",p)
client_moodle.submit('bTcDQRvCITniLCqT38zzd4CaYs8gPsrnjxyZyIVTiTv6DyX0kX', ans)
