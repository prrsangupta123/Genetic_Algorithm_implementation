import numpy
import client_moodle
import random
import heapq



def cal_pop_fitness( pop):
    # Calculating the fitness value of each solution in the current population.
    # The fitness function caulcuates the sum of products between each input and its corresponding weight.
    # fitness = numpy.sum(pop*equation_inputs, axis=1)
    # print("IN HERE")
    fitness =[]
    trainVals=[]
    validVals=[]
    for i in range(0,pop.shape[0]):
        a=list(client_moodle.get_errors('bTcDQRvCITniLCqT38zzd4CaYs8gPsrnjxyZyIVTiTv6DyX0kX',list(pop[i]) ))
        
        trainVals.append(a[0])
        validVals.append(a[1])
        #TANMAYS
            print("Individual :", str(i), "has errors", str(a[0]), str(a[1]),"has fitness\t\t",  pow(a[0], 2)*pow(a[1], 5))
        #MINE
        # print("Individual :", str(i), "has errors", str(a[0]), str(a[1]),"has fitness\t\t",  (a[0]+a[1]))
        #TANMAYS
    fitness=numpy.multiply(numpy.power(numpy.asarray(trainVals), 2), numpy.power(numpy.asarray(validVals), 5)).tolist()
    #MINE
    fitness=numpy.add(numpy.asarray(trainVals), numpy.asarray(validVals)).tolist()
    # print("fitness",fitness)
    #HERE FITNESS IS A LIST
    return (fitness)

def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    # parents = numpy.empty((num_parents, pop.shape[1]))
    # print ("Herer",parents)
    # res = sorted(range(len(fitness)), key = lambda sub: fitness[sub])[-num_parents:] 
    # for i in range(len(res)):
        # print("the parent is ", pop[res[i]], "the fitness is", fitness[res[i]])

    parents = numpy.asarray([x for _, x in sorted(zip(fitness, pop.tolist()))][:num_parents])
    print("Parents is: ", parents)

    #     population = [x for _, x in sorted(zip(array_to_be_used_for_comparison, population))]

    # parents = numpy.random.uniform(low=-10.0, high=10.0, size=(0,0))
    # for j in range(num_parents):
    #     # print("Appending:",pop[res[j]])
    #     parents = numpy.append( arr= parents, values= pop[res[j]])
    #     # print("Iteration number:",j,"  Parents:",parents)
    # parents = parents.reshape(num_parents,11)
    #     # print("parents",parents)
    # # print("parents:",parents)
    # print("parents here on")
    # for i in parents:
    #     print(i)
    return parents

def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually it is at the center.
   

   #ALGORITHM FOR SINGLE POINT CROSSOVER
    # crossover_point = numpy.uint8(offspring_size[1]/2)
    # print("Modularity:",parents.shape[0])
    # for k in range(offspring_size[0]):
    #     # Index of the first parent to mate.
    #     parent1_idx = (k)%parents.shape[0]
    #     # Index of the second parent to mate.
    #     parent2_idx = (k+1)%parents.shape[0]
    #     # The new offspring will have its first half of its genes taken from the first parent.
    #     offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
    #     # The new offspring will have its second half of its genes taken from the second parent.
    #     offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]


    #ALGORRITHM FOR UNIFORM CROSSOVER - 2 PARENTS, k and k+1 mate (WEIGHTED)
    
    # for k in range(offspring_size[0]):
    #     parent1_idx = (k)%parents.shape[0]
    #     parent2_idx = (k+1)%parents.shape[0]

    #     for j in range(0, parents.shape[1]):
    #         x = random.choice([0,1])
    #         if x is 0:
    #             offspring[k,j] = 0.4*parents[parent1_idx,j] + 0.6*parents[parent2_idx,j]
    #         else:
    #             offspring[k,j] = 0.4*parents[parent2_idx,j] + 0.6*parents[parent1_idx,j]
    #ALGORRITHM FOR UNIFORM CROSSOVER - 2 PARENTS, k and k+1 mate (UNWEIGHTED)
    # for k in range(offspring_size[0]):
    #     parent1_idx = (k)%parents.shape[0]
    #     parent2_idx = (k+1)%parents.shape[0]

    #     for j in range(0, parents.shape[1]):
    #         x = random.choice([0,1])
    #         if x is 0:
    #             offspring[k,j] = parents[parent1_idx,j] 
    #         else:
    #             offspring[k,j] = parents[parent2_idx,j] 
    # print("hiii")


    #ALGORITHM FOR UNOFORM CROSSOVER- 2 PARENTS , MOST DIFFERENT PARENTS MATE
    # mates = added.choose_optimal_mates(parents, offspring_size[0])
    

    

    #ALGORITHM FOR UNIFORM CROSSOVER - 2 PARENTS , MORE THAN SOME DIFFERENCE
    # mated = []
    # for q in range(0, parents.shape[0]):
    #     mated.append([])
    # for k in range(0,offspring_size[0]):
    #     parent1_idx = int(numpy.random.uniform(0, parents.shape[0], 1))
    #     parent2_idx = parent1_idx
    #     while numpy.sum(abs(parents[parent1_idx]-parents[[parent2_idx]]))<=1 or \
    #     parent2_idx in  mated[parent1_idx] or parent1_idx in mated[parent2_idx]:
    #         parent2_idx = int(numpy.random.uniform(0, parents.shape[0], 1))
    #     #print("$$$")
    #     for j in range(0, parents.shape[1]):
    #         x = random.choice([0,1])
    #         if x is 0:
    #             offspring[k,j] = parents[parent1_idx,j]
    #         else:
    #             offspring[k,j] = parents[parent2_idx,j]

    for i in range(0, offspring_size[0]):
        parent1 = random.randint(0, len(parents)-1)
        parent2 = random.randint(0, len(parents)-1)
        while parent2==parent1 :
            parent2 = random.randint(0, len(parents)-1)
        print ("parent1 at index number:",parent1,"\t\tValue of parent1", parents[parent1] )
        print ("parent2 at index number:",parent2,"\t\tValue of parent2", parents[parent2] )
        for j in range(0, 11):
            x = random.choice([0,1])
            if x is 0:
                offspring[i,j] = parents[parent1,j] 
            else:
                offspring[i,j] = parents[parent2,j]
        print("offspring created is :", offspring[i])



#ALGORITHM FOR UNIFORM CROSSOVER - 3 PARENTS
    # for k in range(offspring_size[0]):
    #     parent1_idx = (k)%parents.shape[0]
    #     parent2_idx = (k+1)%parents.shape[0]
    #     parent3_idx = (k+2)%parents.shape[0]
    #     weights =[[0.3,0,3,0.4],[0.3,0,4,0.3],[0.4,0,3,0.3]]
        
    #     for j in range(0, parents.shape[1]):
    #         x = random.choice([0,1,2])
    #         offspring[k,j] = weights[x][0]*parents[parent1_idx,j] + weights[x][1]*parents[parent2_idx,j] + weights[x][2] * parents[parent3_idx,j]
    #         if(offspring[k,j]>10):
    #             offspring[k,j]=10
    #         if(offspring[k,j]<-10):
    #             offspring[k,j]=-10
    # print("offspring are: ", offspring)      
    return offspring

def mutation(offspring_crossover):
    #APPROACH 1
    # Mutation changes a single gene in each offspring randomly.
    # for idx in range(offspring_crossover.shape[0]):
    #     # The random value to be added to the gene.
    #     for no_of_mutations in range(0, int(numpy.random.uniform(0,4,1))):
    #         random_value = numpy.random.uniform(-1.0, 1.0, 1)
    #         x = random.choice([0,1])
    #         pos = int(numpy.random.uniform(0, 11, 1))
    #         calcu = offspring_crossover[idx, pos] + random_value*x
            # if calcu>=10:
            #     calcu=10
            # if calcu <=-10:
            #     calcu=-10
            # offspring_crossover[idx,pos] = calcu
    for idx in range(offspring_crossover.shape[0]):
        for j in range(0,offspring_crossover.shape[1]):
            x = random.choice([0,0,1])
            if x==1:
                print("offspring before mutation:", offspring_crossover[idx])
                print("gene changed", j)

                calcu = offspring_crossover[idx,j]
                calcu+=random.choice([+1,-1])*random.uniform(0.9,1.1)*calcu
                if calcu>=10:
                    calcu=10
                if calcu <=-10:
                    calcu=-10
                offspring_crossover[idx,j] = calcu
                print("offspring after mutation:", offspring_crossover)
                



    # print("offspring after mutation are: ", offspring_crossover)
    return offspring_crossover

def create_new_pop(parents,children,num_parents_to_take, num_children_to_take ):
    pop = numpy.random.uniform(low=-10.0, high=10.0, size=(num_children_to_take+ num_parents_to_take,11))
    for i in range (0, num_parents_to_take):
        pop[i]=parents[i]

    for j in range(0,num_children_to_take):
        pop[num_parents_to_take+j] = children[j]

    #print(pop)

    return pop


