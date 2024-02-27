package sudoku.problemdomain;

import java.io.IOException;

public interface IStorage {
    public void updateGameData(SudokuGame game) throws IOException;
    public SudokuGame getGameData() throws IOException;
    
}
