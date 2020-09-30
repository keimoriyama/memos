import React from "react";
import ReactDOM from "react-dom";
import "./index.css";

class Square extends React.Component {
  /* Squareでマス目の状態を管理する必要はないので
  constructor(props) {
    super(props);
    this.state = {
      value: null,
    };
  }
  */
  render() {
    return (
      <button
        className="square"
        onClick={() => {
          this.props.onClick();
        }}
      >
        {this.props.value}
      </button>
    );
  }
}

class Board extends React.Component {
  // stateのリフトアップ部分
  //親コンポーネントであるBoardにstateを管理させる
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
    };
  }

  hanldeClick(i) {
    // 配列のコピーを作成してそれを編集する
    const squares = this.state.squares.slice();
    squares[i] = "X";
    // コピーの内容をもとの配列に反映させる
    this.setState({ squares: squares });
  }
  renderSquare(i) {
    return (
      <Square
        // squareにboardのstateを渡している
        value={this.state.squares[i]}
        // squareにonClickの挙動を渡している
        onClick={() => this.hanldeClick(i)}
      />
    );
  }

  render() {
    const status = "Next player: X";

    return (
      <div>
        <div className="status">{status}</div>
        <div className="board-row">
          {this.renderSquare(0)}
          {this.renderSquare(1)}
          {this.renderSquare(2)}
        </div>
        <div className="board-row">
          {this.renderSquare(3)}
          {this.renderSquare(4)}
          {this.renderSquare(5)}
        </div>
        <div className="board-row">
          {this.renderSquare(6)}
          {this.renderSquare(7)}
          {this.renderSquare(8)}
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
        <div className="game-info">
          <div>{/* status */}</div>
          <ol>{/* TODO */}</ol>
        </div>
      </div>
    );
  }
}

// ========================================

ReactDOM.render(<Game />, document.getElementById("root"));
