import java.util.*;

class RideSharingSystem {

    private Queue<Integer> drivers;
    private LinkedHashSet<Integer> riders;

    public RideSharingSystem() {
        drivers = new ArrayDeque<>();
        riders = new LinkedHashSet<>();
    }

    public void addRider(int riderId) {
        riders.add(riderId);
    }

    public void addDriver(int driverId) {
        drivers.offer(driverId);
    }

    public int[] matchDriverWithRider() {
        if (drivers.isEmpty() || riders.isEmpty()) {
            return new int[]{-1, -1};
        }

        int driverId = drivers.poll();

        // Get earliest rider
        Iterator<Integer> it = riders.iterator();
        int riderId = it.next();
        it.remove();

        return new int[]{driverId, riderId};
    }

    public void cancelRider(int riderId) {
        riders.remove(riderId);
    }
}
