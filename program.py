import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
import sys
import splitter as splt
import create_data_for_assignment as cret
import combine_images as com

zoom, corruption = 0.2, 0.7

if len(sys.argv) > 2:
    if sys.argv[1] == '0': # reconstruct the given incomplete image
        dir_name = sys.argv[2]
        A_inv = np.load(dir_name + "/A_inv.npy")
        C = np.load(dir_name + "/C.npy")
        y = np.load(dir_name + "/y.npy")

        print("A_inv.shape",A_inv.shape)
        print("C.shape",C.shape)
        print("y.shape",y.shape)

        k, n = C.shape

        # Construct the problem.
        s = cp.Variable(shape=(n,1))

        objective = cp.Minimize( cp.norm(s,1)  )
        constraint = [ (cp.norm(y - C*s, 2)) <= 1e-5 ]

        prob = cp.Problem(objective, constraint)

        prob.solve(solver=None, verbose=True)
        print("s.shape", s.shape)
        ls = [each[0] for each in s.value]

        x = np.dot(A_inv, np.array(ls))

        x = np.transpose(x.reshape(100, 100))
        plt.imshow(x, cmap='gray')
        plt.title("Reconstructed")
        plt.show()
        plt.imsave('Reconstructed/recons_given_heat.png', x)
        plt.imsave('Reconstructed/recons_given_grayscale.png', x, cmap='gray')

    if sys.argv[1] == '1': # use our image, split, create data, reconstruct, combine
        target_image = sys.argv[2]
        splt.split(target_image)
        images = ['our_data/R.png', 'our_data/G.png', 'our_data/B.png']
        dest = ['our_data/R/', 'our_data/G/', 'our_data/B/']
        for i in range(3):
            cret.run(images[i], dest[i], zoom, corruption)

            A_inv = np.load(dest[i] + "/A_inv.npy")
            C = np.load(dest[i] + "/C.npy")
            y = np.load(dest[i] + "/y.npy")

            print("A_inv.shape",A_inv.shape)
            print("C.shape",C.shape)
            print("y.shape",y.shape)

            k, n = C.shape

            # Construct the problem.
            s = cp.Variable(shape=(n,1))

            objective = cp.Minimize( cp.norm(s,1)  )
            constraint = [ (cp.norm(y - C*s, 2)) <= 1e-5 ]

            prob = cp.Problem(objective, constraint)

            prob.solve(solver=None, verbose=True)
            print("s.shape", s.shape)
            ls = [each[0] for each in s.value]

            x = np.dot(A_inv, np.array(ls))

            np.save(dest[i] + "s_vec", x)
        com.combine(int(zoom*100))